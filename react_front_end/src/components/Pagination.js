const Pagination = ({ pageQuery, setPageQuery }) => {

  const handlePreviosPage = (e) => {
    e.preventDefault();
    setPageQuery([parseInt(pageQuery[0]) - 1]);
  };

  const handleNextPage = (e) => {
    e.preventDefault();
    setPageQuery([parseInt(pageQuery[0]) + 1]);
  };

  // Data I will need fot the pagination
  // results.has_previous
  // results.previous_page_number
  // results.paginator.page_range
  // results.number
  // results.paginator.num_pages
  // results.number|add:"-1"
  // results.number|add:"1"
  // results.number|add:"-2"
  // results.number|add:"2"
  // results.has_next
  // results.next_page_number

  return (
    <nav className="govuk-pagination" role="navigation" aria-label="Pagination">
      {/* {% if results.has_previous %} */}
      <div className="govuk-pagination__prev">
        <a className="govuk-link govuk-pagination__link govuk-link--no-visited-state" href="" onClick={handlePreviosPage}>
          <svg className="govuk-pagination__icon govuk-pagination__icon--prev" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
            <path d="m6.5938-0.0078125-6.7266 6.7266 6.7441 6.4062 1.377-1.449-4.1856-3.9768h12.896v-2h-12.984l4.2931-4.293-1.414-1.414z"></path>
          </svg>
          <span className="govuk-pagination__link-title">Previous<span className="govuk-visually-hidden"> page</span></span>
        </a>
      </div>
      {/* {% endif %} */}
      <ul className="govuk-pagination__list">
        {/* {% for page_number in results.paginator.page_range %} */}
        {/* {% if page_number == results.number %} */}
        <li className="govuk-pagination__item govuk-pagination__item--current">
          <a className="govuk-link govuk-pagination__link govuk-link--no-visited-state" href="" aria-current="page">
            {pageQuery[0]}
          </a>
        </li>
        {/* {% elif page_number == 1 or page_number == results.paginator.num_pages or page_number == results.number|add:"-1" or page_number == results.number|add:"1" %} */}
        <li className="govuk-pagination__item">
          <a className="govuk-link govuk-pagination__link govuk-link--no-visited-state" href="">{pageQuery[0]}</a>
        </li>
        {/* {% elif page_number == results.number|add:"-2" or page_number == results.number|add:"2" %} */}
        <li className="govuk-pagination__item govuk-pagination__item--ellipses">&hellip;</li>
        {/* {% endif %} */}
        {/* {% endfor %} */}
      </ul>
      {/* {% if results.has_next %} */}
      <div className="govuk-pagination__next">
        <a className="govuk-link govuk-pagination__link govuk-link--no-visited-state" href="" onClick={handleNextPage}>
          <span className="govuk-pagination__link-title">Next<span className="govuk-visually-hidden"> page</span></span>
          <svg className="govuk-pagination__icon govuk-pagination__icon--next" xmlns="http://www.w3.org/2000/svg" height="13" width="15" aria-hidden="true" focusable="false" viewBox="0 0 15 13">
            <path d="m8.107-0.0078125-1.4136 1.414 4.2926 4.293h-12.986v2h12.896l-4.1855 3.9766 1.377 1.4492 6.7441-6.4062-6.7246-6.7266z"></path>
          </svg>
        </a>
      </div>
      {/* {% endif %} */}
    </nav>
  );
}

export { Pagination };
