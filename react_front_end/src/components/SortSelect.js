const SortSelect = ({
  sortQuery,
  setSortQuery
}) => {

  const handleSortChange = (e) => {
    setSortQuery([e.target.value]);
  };

  return (
    <div className="govuk-form-group">
      <label className="govuk-label" htmlFor="sort-select">
        Sort by
      </label>
      <select className="govuk-select" value={sortQuery[0]} onChange={handleSortChange} id="sort-select">
        <option value="recent">Recently updated</option>
        <option value="relevance">Relevance</option>
      </select>
    </div>
  );
}

export { SortSelect };
