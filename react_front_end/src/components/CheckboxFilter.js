const CheckboxFilter = ({ checkboxData, checkedState, setCheckedState, setQueryParams }) => {

  const handleOnChange = (position) => {
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
    <div className="govuk-checkboxes govuk-checkboxes--small" data-module="govuk-checkboxes">
      {checkboxData.map(({ name, label }, index) => (
        <div className="govuk-checkboxes__item" key={index}>
          <input
            className="govuk-checkboxes__input"
            type="checkbox"
            id={`${name}-${index}`}
            name={name}
            value={name}
            checked={checkedState[index]}
            onChange={() => handleOnChange(index)}
          />
          <label className="govuk-label govuk-checkboxes__label" htmlFor={`${name}-${index}`}>{label}</label>
        </div>
      ))}
    </div>
  )
};

export { CheckboxFilter };
