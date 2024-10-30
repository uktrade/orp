import { useState, useEffect } from 'react';
import { useQueryParams } from './hooks/useQueryParams';
import { Search } from './components/Search';
import { CheckboxFilter } from './components/CheckboxFilter';
import { AppliedFilters } from './components/AppliedFilters';
import { Results } from './components/Results';
import { Pagination } from './components/Pagination';
import { SortSelect } from './components/SortSelect';
import { documentType, publisher } from './utils/filters';

const generateCheckedState = (checkboxes, queryValues) => checkboxes.map(({ name }) => queryValues.includes(name))

function App() {
  const [searchQuery, setSearchQuery] = useQueryParams('search', []);
  const [docTypeQuery, setDocTypeQuery] = useQueryParams('document_type', []);
  const [publisherQuery, setPublisherQuery] = useQueryParams('publisher', []);
  const [sortQuery, setSortQuery] = useQueryParams('sort', ['recent']);
  const [pageQuery, setPageQuery] = useQueryParams('page', [1]);


  // Set initial checked state as array of booleans for checkboxes based on query params
  const [documentTypeCheckedState, setDocumentTypeCheckedState] = useState(generateCheckedState(documentType, docTypeQuery));
  const [publisherCheckedState, setPublisherCheckedState] = useState(generateCheckedState(publisher, publisherQuery));

  const handleSearchChange = (event) => {
    setSearchQuery([event.target.value]);
  };

  const handleDeleteFilter = (filterName, filter) => {
    const updateQueryAndState = (query, setQuery, setCheckedState, data) => {
      const updatedQuery = query.filter(item => item !== filter);
      setQuery(updatedQuery);
      setCheckedState(generateCheckedState(data, updatedQuery));
    };

    if (filterName === 'docType') {
      updateQueryAndState(docTypeQuery, setDocTypeQuery, setDocumentTypeCheckedState, documentType);
    } else if (filterName === 'publisher') {
      updateQueryAndState(publisherQuery, setPublisherQuery, setPublisherCheckedState, publisher);
    }
  };

  const fetchData = async (queryString) => {
    try {
      const response = await fetch(`/api/data?${queryString}`);
      const data = await response.json();
      console.log(data); // Handle the fetched data
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    const handler = setTimeout(() => {
      if (searchQuery.length > 0 || docTypeQuery.length > 0 || publisherQuery.length > 0) {
        const queryString = new URLSearchParams({
          search: searchQuery.join(','),
          document_type: docTypeQuery.join(','),
          publisher: publisherQuery.join(',')
        }).toString();

        // fetchData(queryString);
        console.log("Fetching data with query string:", queryString);
      }
    }, 300); // Adjust the delay as needed

    return () => {
      clearTimeout(handler);
    };
  }, [searchQuery, docTypeQuery, publisherQuery]);

  return (
    <div className="govuk-grid-row search-form">
      <div className="govuk-grid-column-one-third">
        <Search handleSearchChange={handleSearchChange} searchQuery={searchQuery} />
        <div className="govuk-form-group ">
          <fieldset className="govuk-fieldset">
            <legend className="govuk-fieldset__legend govuk-fieldset__legend--m">
              <h2 className="govuk-fieldset__heading">
                Document types
              </h2>
            </legend>
            <CheckboxFilter
              checkboxData={documentType}
              checkedState={documentTypeCheckedState}
              setCheckedState={setDocumentTypeCheckedState}
              setQueryParams={setDocTypeQuery}
            />
          </fieldset>
        </div>
        <div className="govuk-form-group ">
          <fieldset className="govuk-fieldset">
            <legend className="govuk-fieldset__legend govuk-fieldset__legend--m">
              <h2 className="govuk-fieldset__heading">
                Published by
              </h2>
            </legend>
            <CheckboxFilter
              checkboxData={publisher}
              checkedState={publisherCheckedState}
              setCheckedState={setPublisherCheckedState}
              setQueryParams={setPublisherQuery}
            />
          </fieldset>
        </div>
      </div>
      <div className="govuk-grid-column-two-thirds">
        {docTypeQuery.length > 0 || publisherQuery.length > 0 ? (
          <AppliedFilters
            documentTypeCheckedState={documentTypeCheckedState}
            publisherCheckedState={publisherCheckedState}
            removeFilter={handleDeleteFilter}
          />
        ) : null}
        <SortSelect sortQuery={sortQuery} setSortQuery={setSortQuery} />
        <Results
          searchQuery={searchQuery}
          docTypeQuery={docTypeQuery}
          publisherQuery={publisherQuery}
          pageQuery={pageQuery}
          sortQuery={sortQuery}
        />
        <Pagination pageQuery={pageQuery} setPageQuery={setPageQuery} />
      </div>
    </div>
  );
}

export default App;
