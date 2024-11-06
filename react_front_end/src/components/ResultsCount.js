function ResultsCount({ totalResults, isLoading }) {
  return (
    <p className="govuk-body govuk-!-font-weight-bold govuk-!-margin-bottom-0">
      {isLoading ? "Loading..." : totalResults ? `${totalResults} results` : "No results found"}
    </p>
  )
}

export { ResultsCount }
