function NoResultsContent() {
  return (
    <>
      <h2 className="govuk-heading-l">There are no matching results</h2>
      <p className="govuk-body-m">Improve your results by:</p>
      <ul className="govuk-list govuk-list--bullet">
        <li className="govuk-body-m">removing filters</li>
        <li className="govuk-body-m">double-checking your spelling</li>
        <li className="govuk-body-m">using fewer keywords</li>
        <li className="govuk-body-m">searching for something less specific</li>
      </ul>

      <details className="govuk-details">
        <summary className="govuk-details__summary">
          <span className="govuk-details__summary-text">Help with searching</span>
        </summary>
        <div className="govuk-details__text">
          <p className="govuk-body">You can use:</p>
          <ul className="govuk-list govuk-list--bullet">
            <li className="govuk-body-m">quotes for results that include a phrase. For example, "health and safety"</li>
            <li className="govuk-body-m">
              commas to see results that include any of your keywords. For example, lifting, equipment, machinery
            </li>
            <li className="govuk-body-m">
              + with no spaces to see results that include all your keywords. For example, asbestos+handling
            </li>
          </ul>
        </div>
      </details>
    </>
  )
}

export { NoResultsContent }
