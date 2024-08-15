function Search({ filters, setFilters }) {
  const { searchString } = filters;
  const handleChange = (event) => {
    setFilters({
      ...filters,
      [event.target.name]: event.target.value
    });
  }

  return (
    <div className="search-form">
      <form>
        <div className="govuk-form-group">
          <label className="govuk-label" htmlFor="search">Search keywords</label>
          <input className="govuk-input" id="searchString" name="searchString" type="text" onChange={handleChange} value={searchString} />
        </div>
        <div className="govuk-form-group">
          <button className="govuk-button" type="submit">Search regulations</button>
        </div>
      </form>
    </div>
  )
}

export { Search }