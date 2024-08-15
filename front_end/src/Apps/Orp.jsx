import { useState, useEffect } from 'react'
import { Search } from '../Components/Search.jsx'
import { Filters } from '../Components/Filters.jsx'
import { Results } from '../Components/Results.jsx'
import { FiltersFromOrp } from '../Components/FiltersFromOrp.jsx'

function buildQuery(filters) {
  const { searchString, numberOfResults } = filters
  const limitQuery = ` LIMIT ${numberOfResults}`
  let query = 'SELECT c FROM S3Object[*].barriers[*] c'

  if (searchString && searchString.length > 2) {
    query += ` WHERE LOWER(c.title) LIKE LOWER('%${searchString}%') OR LOWER(c.summary) LIKE LOWER('%${searchString}%')`
  }

  query += limitQuery

  return query
}


function App() {
  const [results, setResults] = useState(null)
  const [filters, setFilters] = useState({
    searchString: '',
    numberOfResults: 10,
  })


  const DATA_API_URL = 'https://data.api.trade.gov.uk/v1/'
  const DATASET = 'market-barriers'
  const VERSION = 'v1.0.10'
  const FORMAT = 'json'
  const S3_QUERY = buildQuery(filters)
  const ENCODED_S3_QUERY = encodeURI(S3_QUERY);
  const URL = `${DATA_API_URL}datasets/${DATASET}/versions/${VERSION}/data?format=${FORMAT}&query-s3-select=${ENCODED_S3_QUERY}`

  useEffect(() => {
    if (filters.searchString !== '' && filters.searchString.length < 3) {
      return
    }

    console.log("Searching for: ", filters)

    const timeout = setTimeout(() => {
      fetch(URL)
        .then((response) => response.json())
        .then((data) => setResults(data))
      // .then((data) => console.log(data))
    }, 500)

    return () => clearTimeout(timeout)


    // fetch(URL)
    //   .then((response) => response.json())
    //   .then((data) => setResults(data))
    //   .then((data) => console.log(data))
  }, [filters])

  return (
    <>
      <div className="govuk-grid-row">
        <div className="govuk-grid-column-two-thirds">
          <h1 className="govuk-heading-xl">Find regulations</h1>
          <p className="govuk-body govuk-body-s">From: Department for Business and Trade</p>
          <div className="govuk-inset-text">This does not include all regulations. It will be updated with more in the future.</div>
        </div>
      </div>
      <div className="govuk-grid-row">
        <div className="govuk-grid-column-one-third">
          <Search filters={filters} setFilters={setFilters} />
          <Filters filters={filters} setFilters={setFilters} />
          <FiltersFromOrp filters={filters} setFilters={setFilters} />
        </div>
        <div className="govuk-grid-column-two-thirds">
          <div className="results">
            <h2 className="govuk-heading-m">Results{!results ? "" : `: ${results.rows.length} regulations`}</h2>
            {!results ? <p>Loading</p> : <Results results={results} />}
          </div>
        </div>
      </div>
    </>
  )
}

export default App
