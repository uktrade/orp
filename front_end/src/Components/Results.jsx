function Results({ results }) {
  return (
    <ul className="govuk-list">
      {results.rows.map((result) => {
        const { title, id, summary, status_date } = result.c;

        const concatSummary = summary.length > 200 ? summary.substring(0, 200) + "..." : summary;

        return (
          <li key={id}>
            <hr className="govuk-section-break govuk-section-break--l govuk-section-break--visible" />
            <p className="govuk-body govuk-!-font-weight-bold">
              <a href="#" className="govuk-link govuk-link--no-underline">{title}</a>
            </p>
            <p className="govuk-body">
              {concatSummary}
            </p>
            <p className="govuk-body">
              {status_date}
            </p>
          </li>
        )
      })}
    </ul>
  )
}

export { Results }