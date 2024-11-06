function Search({ handleSearchChange, searchQuery, handleSearchSubmit }) {
  const handleSubmit = (event) => {
    event.preventDefault()
    handleSearchSubmit()
  }

  return (
    <div className="govuk-form-group search-group">
      <label className="govuk-label" htmlFor="search">
        Search
      </label>
      <form onSubmit={handleSubmit} className="search-input-button">
        <input
          id="search"
          className="govuk-input search-input"
          name="search"
          type="search"
          onChange={handleSearchChange}
          value={searchQuery}
          aria-label="Search input"
        />
        <button type="submit" className="search__button" aria-label="Submit search">
          <span className="govuk-visually-hidden">Submit search</span>
        </button>
      </form>
    </div>
  )
}

export { Search }
