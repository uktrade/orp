function Pagination({ pageQuery, setPageQuery }) {
  const handlePreviousPage = (e) => {
    e.preventDefault()
    setPageQuery([parseInt(pageQuery[0]) - 1])
  }

  const handleNextPage = (e) => {
    e.preventDefault()
    setPageQuery([parseInt(pageQuery[0]) + 1])
  }

  // Data I will need fot the pagination
  // results.has_previous
  // results.previous_page_number
  // results.paginator.page_range
  // results.number
  // results.paginator.num_pages
  // results.has_next
  // results.next_page_number
  const results = {
    has_previous: true,
    previous_page_number: 1,
    paginator: {
      page_range: [1, 2, 3, 4, 5],
      num_pages: 5,
    },
    number: 1,
    has_next: true,
    next_page_number: 2,
  }

  return (
    <nav className="govuk-pagination" role="navigation" aria-label="Pagination">
      {results.has_previous && (
        <div className="govuk-pagination__prev">
          <a
            className="govuk-link govuk-pagination__link govuk-link--no-visited-state"
            href="#"
            onClick={handlePreviousPage}
            aria-label="Previous page"
          >
            <svg
              className="govuk-pagination__icon govuk-pagination__icon--prev"
              xmlns="http://www.w3.org/2000/svg"
              height="13"
              width="15"
              aria-hidden="true"
              focusable="false"
              viewBox="0 0 15 13"
            >
              <path d="m6.5938-0.0078125-6.7266 6.7266 6.7441 6.4062 1.377-1.449-4.1856-3.9768h12.896v-2h-12.984l4.2931-4.293-1.414-1.414z"></path>
            </svg>
            <span className="govuk-pagination__link-title">
              Previous<span className="govuk-visually-hidden"> page</span>
            </span>
          </a>
        </div>
      )}
      <ul className="govuk-pagination__list">
        {results.paginator.page_range.map((page_number) => (
          <li key={page_number} className="govuk-pagination__item">
            <a
              className={`govuk-link govuk-pagination__link ${results.number === page_number ? "govuk-pagination__link--current" : ""}`}
              href="#"
              onClick={(e) => {
                e.preventDefault()
                setPageQuery([page_number])
              }}
              aria-current={results.number === page_number ? "page" : undefined}
            >
              {page_number}
            </a>
          </li>
        ))}
      </ul>
      {results.has_next && (
        <div className="govuk-pagination__next">
          <a
            className="govuk-link govuk-pagination__link govuk-link--no-visited-state"
            href="#"
            onClick={handleNextPage}
            aria-label="Next page"
          >
            <span className="govuk-pagination__link-title">
              Next<span className="govuk-visually-hidden"> page</span>
            </span>
            <svg
              className="govuk-pagination__icon govuk-pagination__icon--next"
              xmlns="http://www.w3.org/2000/svg"
              height="13"
              width="15"
              aria-hidden="true"
              focusable="false"
              viewBox="0 0 15 13"
            >
              <path d="m8.4062 13.007 6.7266-6.7266-6.7441-6.4062-1.377 1.449 4.1856 3.9768h-12.896v2h12.984l-4.2931 4.293 1.414 1.414z"></path>
            </svg>
          </a>
        </div>
      )}
    </nav>
  )
}

export { Pagination }
