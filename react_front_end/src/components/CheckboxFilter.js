import { useState, useEffect } from 'react';

const CheckboxFilter = ({ checkboxData, checkedState, setCheckedState, setQueryParams, withSearch }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [filteredData, setFilteredData] = useState(checkboxData);

  useEffect(() => {
    setFilteredData(
      checkboxData.filter(({ label }) =>
        label.toLowerCase().includes(searchQuery.toLowerCase())
      )
    );
  }, [searchQuery, checkboxData]);


  const handleCheckboxChange = (position) => {
    const updatedCheckedState = checkedState.map((item, index) =>
      index === position ? !item : item
    );

    // Generate an array of the names of all checked checkboxes
    const checkedItems = checkboxData
      .filter((_, index) => updatedCheckedState[index])
      .map(({ name }) => name);

    setQueryParams(checkedItems);
    setCheckedState(updatedCheckedState);
  }



  return (
    <>
      {withSearch ? <SearchCheckboxes searchQuery={searchQuery} setSearchQuery={setSearchQuery} /> : null}
      <div className={`govuk-checkboxes govuk-checkboxes--small ${withSearch ? 'orp-max-height-250' : ""}`} data-module="govuk-checkboxes">
        {filteredData.map(({ name, label }, index) => (
          <div className="govuk-checkboxes__item" key={index}>
            <input
              className="govuk-checkboxes__input"
              type="checkbox"
              id={`${name}-${index}`}
              name={name}
              value={name}
              checked={checkedState[index]}
              onChange={() => handleCheckboxChange(index)}
            />
            <label className="govuk-label govuk-checkboxes__label" htmlFor={`${name}-${index}`}>{label}</label>
          </div>
        ))}
      </div>
    </>
  )
};

const SearchCheckboxes = ({ searchQuery, setSearchQuery }) => {

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  }

  return (
    <div className="govuk-form-group search-group">
      <label className="govuk-label govuk-visually-hidden" htmlFor="input-autocomplete">
        Search by publisher
      </label>
      <div className="search-input-button search-input-button--black orp-publisher-search">
        <input
          className="govuk-input orp-publisher-search__input app-site-search__input--default"
          id="input-autocomplete"
          name="input-autocomplete"
          type="search"
          placeholder="Search"
          value={searchQuery}
          onChange={handleSearchChange}
          role="combobox"
        />
      </div>
    </div>
  )
}

export { CheckboxFilter };
