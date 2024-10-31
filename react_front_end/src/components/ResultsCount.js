const ResultsCount = () => {
  // const { searchQuery, docTypeQuery, publisherQuery } = useQueryParams();
  // const { data, isLoading } = useSearchResults(searchQuery, docTypeQuery, publisherQuery);

  // Mocked data for testing purposes
  const data = { totalResults: 0 }
  const isLoading = false

  const { totalResults } = data || {}

  return (
    <p className="govuk-body govuk-!-font-weight-bold govuk-!-margin-bottom-0">
      {isLoading ? "Loading..." : totalResults ? `${totalResults} results` : "No results found"}
    </p>
  )
}

export { ResultsCount }
