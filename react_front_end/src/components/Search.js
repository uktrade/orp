const Search = ({ handleSearchChange, searchQuery }) => {
  return (
    <div className="govuk-form-group search-group">
      <label className="govuk-label" htmlFor="search">
        Search
      </label>
      <div className="search-input-button">
        <input
          id="search"
          className="govuk-input search-input"
          name="search"
          type="search"
          onChange={handleSearchChange}
          value={searchQuery}
        />
        <button type="submit" className="search__button"></button>
      </div>
    </div>
  )
};

export { Search };
