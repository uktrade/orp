import { useState, useEffect, useMemo, useCallback } from "react"
import { useQueryParams } from "./hooks/useQueryParams"
import { fetchData } from "./utils/fetch-drf"
import { DOCUMENT_TYPES, PUBLISHERS } from "./utils/constants"

import { Search } from "./components/Search"
import { CheckboxFilter } from "./components/CheckboxFilter"
import { AppliedFilters } from "./components/AppliedFilters"
import { Results } from "./components/Results"
import { Pagination } from "./components/Pagination"
import { ResultsCount } from "./components/ResultsCount"
import { SortSelect } from "./components/SortSelect"
import { NoResultsContent } from "./components/NoResultsContent"

const generateCheckedState = (checkboxes, queryValues) => checkboxes.map(({ name }) => queryValues.includes(name))

function App() {
  const [searchInput, setSearchInput] = useState(useQueryParams("search")[0] || "")
  const [searchQuery, setSearchQuery] = useQueryParams("search", [])
  const [docTypeQuery, setDocTypeQuery] = useQueryParams("document_type", [])
  const [publisherQuery, setPublisherQuery] = useQueryParams("publisher", [])
  const [sortQuery, setSortQuery] = useQueryParams("sort", ["recent"])
  const [pageQuery, setPageQuery] = useQueryParams("page", [1])
  const [data, setData] = useState([])
  const [isLoading, setIsLoading] = useState(true)

  // Memoize the initial checked state for document types and publishers
  const initialDocumentTypeCheckedState = useMemo(
    () => generateCheckedState(DOCUMENT_TYPES, docTypeQuery),
    [docTypeQuery],
  )
  const initialPublisherCheckedState = useMemo(() => generateCheckedState(PUBLISHERS, publisherQuery), [publisherQuery])

  // Set initial checked state as array of booleans for checkboxes based on query params
  const [documentTypeCheckedState, setDocumentTypeCheckedState] = useState(initialDocumentTypeCheckedState)
  const [publisherCheckedState, setPublisherCheckedState] = useState(initialPublisherCheckedState)

  // Memoize the handleSearchChange function
  const handleSearchChange = useCallback(
    (event) => {
      setSearchInput(event.target.value)
    },
    [setSearchInput],
  )

  const handleDeleteFilter = (filterName, filter) => {
    const updateQueryAndState = (query, setQuery, setCheckedState, data) => {
      const updatedQuery = query.filter((item) => item !== filter)
      setQuery(updatedQuery)
      setCheckedState(generateCheckedState(data, updatedQuery))
    }

    if (filterName === "docType") {
      updateQueryAndState(docTypeQuery, setDocTypeQuery, setDocumentTypeCheckedState, DOCUMENT_TYPES)
    } else if (filterName === "publisher") {
      updateQueryAndState(publisherQuery, setPublisherQuery, setPublisherCheckedState, PUBLISHERS)
    }
  }

  const handleClearFilters = (event) => {
    event.preventDefault()
    setDocTypeQuery([])
    setPublisherQuery([])
    setDocumentTypeCheckedState(generateCheckedState(DOCUMENT_TYPES, []))
    setPublisherCheckedState(generateCheckedState(PUBLISHERS, []))
  }

  const fetchDataWithLoading = async (queryString) => {
    setIsLoading(true)
    try {
      const data = await fetchData(queryString)
      setData(data)
    } catch (error) {
      console.error("Error fetching data:", error)
    } finally {
      setIsLoading(false)
    }
  }

  const handleSearchSubmit = useCallback(() => {
    setSearchQuery([searchInput])
    // setPageQuery([1])

    const filterParams = {
      ...(searchInput.length > 0 && { search: searchInput }),
      ...(docTypeQuery.length > 0 && { document_type: docTypeQuery }),
      ...(publisherQuery.length > 0 && { publisher: publisherQuery }),
      sort: sortQuery.join(","),
      page: 1,
    }

    fetchDataWithLoading(filterParams)
  }, [searchInput, docTypeQuery, publisherQuery, sortQuery])

  useEffect(() => {
    const handler = setTimeout(() => {
      // This version is to send to the Django backend
      // const queryString = new URLSearchParams({
      //   ...(searchQuery.length > 2 && { search: searchQuery.join(",") }),
      //   ...(docTypeQuery.length > 0 && { document_type: docTypeQuery.join(",") }),
      //   ...(publisherQuery.length > 0 && { publisher: publisherQuery.join(",") }),
      //   sort: sortQuery,
      //   page: pageQuery,
      // }).toString()

      // This version is for the S3 query
      const filterParams = {
        ...(searchQuery.length > 0 && { search: searchQuery.join(",") }),
        ...(docTypeQuery.length > 0 && { document_type: docTypeQuery }),
        ...(publisherQuery.length > 0 && { publisher: publisherQuery }),
        sort: sortQuery.join(","),
        page: pageQuery.join(","),
      }

      fetchDataWithLoading(filterParams)
    }, 300) // Adjust the delay as needed

    return () => {
      clearTimeout(handler)
    }
  }, [docTypeQuery, publisherQuery, sortQuery, pageQuery])

  return (
    <div className="govuk-grid-row search-form">
      <div className="govuk-grid-column-one-third">
        <Search
          handleSearchChange={handleSearchChange}
          searchInput={searchInput}
          handleSearchSubmit={handleSearchSubmit}
        />
        <div className="govuk-form-group ">
          <fieldset className="govuk-fieldset">
            <legend className="govuk-fieldset__legend govuk-fieldset__legend--m">
              <h2 className="govuk-fieldset__heading">Document types</h2>
            </legend>
            <CheckboxFilter
              checkboxData={DOCUMENT_TYPES}
              checkedState={documentTypeCheckedState}
              setCheckedState={setDocumentTypeCheckedState}
              setQueryParams={setDocTypeQuery}
              withSearch={false}
              setIsLoading={setIsLoading}
            />
          </fieldset>
        </div>
        <div className="govuk-form-group">
          <fieldset className="govuk-fieldset">
            <legend className="govuk-fieldset__legend govuk-fieldset__legend--m">
              <h2 className="govuk-fieldset__heading">Published by</h2>
            </legend>
            <CheckboxFilter
              checkboxData={PUBLISHERS}
              checkedState={publisherCheckedState}
              setCheckedState={setPublisherCheckedState}
              setQueryParams={setPublisherQuery}
              withSearch={true}
              setIsLoading={setIsLoading}
            />
          </fieldset>
        </div>
        <hr className="govuk-section-break govuk-section-break--m govuk-section-break--visible" />
        <p className="govuk-body">
          <a
            id="download-csv-link"
            href={`download_csv/?${new URLSearchParams({
              search: searchQuery.join(","),
              document_type: docTypeQuery.join(","),
              publisher: publisherQuery.join(","),
              sort: sortQuery.join(","),
              page: pageQuery.join(","),
            }).toString()}`}
            className="govuk-link govuk-link--no-visited-state govuk-!-float-right"
          >
            Download search results as CSV file
          </a>
        </p>
      </div>
      <div className="govuk-grid-column-two-thirds">
        <div className="orp-flex orp-flex--space-between">
          <ResultsCount
            isLoading={isLoading}
            start={data.start_index}
            end={data.end_index}
            totalResults={data.results_total_count}
          />
          <p className="govuk-body govuk-!-margin-bottom-0">
            <a
              href=""
              onClick={handleClearFilters}
              className="govuk-link govuk-link--no-visited-state
                    "
            >
              Clear all filters
            </a>
          </p>
        </div>
        {docTypeQuery.length > 0 || publisherQuery.length > 0 ? (
          <AppliedFilters
            documentTypeCheckedState={documentTypeCheckedState}
            publisherCheckedState={publisherCheckedState}
            removeFilter={handleDeleteFilter}
          />
        ) : (
          <hr className="govuk-section-break govuk-section-break--m govuk-section-break--visible" />
        )}
        <SortSelect sortQuery={sortQuery} setSortQuery={setSortQuery} />
        <hr className="govuk-section-break govuk-section-break--m govuk-section-break--visible" />
        {data.results_total_count === 0 && !isLoading ? (
          <NoResultsContent />
        ) : (
          <Results results={data.results} isLoading={isLoading} searchQuery={searchQuery} />
        )}

        <Pagination pageData={data} pageQuery={pageQuery} setPageQuery={setPageQuery} />
      </div>
    </div>
  )
}

export default App
