function NoResultsContent() {
  return (
    <>
      <h2 className="govuk-heading-l">There are no matching results</h2>
      <p className="govuk-body-m">Improve your search results by:</p>
      <ul className="govuk-list govuk-list--bullet">
        <li className="govuk-body-m">removing filters</li>
        <li className="govuk-body-m">double-checking your spelling</li>
        <li className="govuk-body-m">using fewer keywords</li>
        <li className="govuk-body-m">searching for something less specific</li>
      </ul>
      <h3 className="govuk-heading-m">Related searches</h3>
      <p className="govuk-body">Try these related search terms.</p>
      <ul className="govuk-list">
        <li className="govuk-body">
          <a className="govuk-link" href="/?search=construction+site+safety">
            construction site safety
          </a>
        </li>
        <li className="govuk-body">
          <a className="govuk-link" href="/?search=building+site+safety">
            building site safety
          </a>
        </li>
        <li className="govuk-body">
          <a className="govuk-link" href="/?search=aggregate+use">
            aggregate use
          </a>
        </li>
      </ul>
    </>
  )
}

export { NoResultsContent }
