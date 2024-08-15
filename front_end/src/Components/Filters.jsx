function Filters({ filters, setFilters }) {
  const { numberOfResults } = filters;

  const handleChange = (event) => {
    setFilters({
      ...filters,
      [event.target.name]: event.target.value
    });
  }

  return (
    <div className="filter-form">
      <h2 className="govuk-heading-m">Filter results</h2>
      <form>
        <div className="govuk-form-group">
          <label className="govuk-label" htmlFor="filter">Number of results to show</label>
          <select className="govuk-select" id="numberOfResults" name="numberOfResults" onChange={handleChange} value={numberOfResults}>
            <option value="10">Show 10</option>
            <option value="20">Show 20</option>
            <option value="50">Show 50</option>
          </select>
        </div>
        <div className="govuk-form-group">
          <button className="govuk-button" type="submit">Apply filters</button>
        </div>
      </form>
    </div>
  )
}

export { Filters }