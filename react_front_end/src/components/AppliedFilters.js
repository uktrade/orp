import { DOCUMENT_TYPES, PUBLISHERS } from "../utils/constants"

function AppliedFilters({ documentTypeCheckedState, publisherCheckedState, removeFilter }) {
  // Combine checked document types and publishers into a single array
  const checkedFilters = [
    ...documentTypeCheckedState
      .map((item, index) => (item ? { type: "docType", ...DOCUMENT_TYPES[index] } : null))
      .filter((item) => item !== null),
    ...publisherCheckedState
      .map((item, index) => (item ? { type: "publisher", ...PUBLISHERS[index] } : null))
      .filter((item) => item !== null),
  ]

  return (
    <ul className="orp-applied-filters-container">
      {checkedFilters.map((filter, index) => (
        <li className="orp-applied-filter-tag" key={index}>
          <a href="#delete" onClick={() => removeFilter(filter.type, filter.name)}>
            <span className="govuk-visually-hidden">Remove filter:</span>
            <span className="govuk-body-s">{filter.label}</span>
          </a>
        </li>
      ))}
    </ul>
  )
}

export { AppliedFilters }
