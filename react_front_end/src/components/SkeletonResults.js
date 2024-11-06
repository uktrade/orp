function SkeletonResults() {
  return (
    <ul className="govuk-list skeleton-wrapper">
      {Array.from({ length: 5 }).map((_, index) => (
        <li key={index}>
          <div className="skeleton-type"></div>
          <div className="skeleton-title"></div>
          <div className="skeleton-description"></div>
          <div className="skeleton-description"></div>
          <div className="skeleton-description"></div>
          <div className="skeleton-published"></div>
          <div className="skeleton-date"></div>
          <div className="skeleton-topics"></div>
          <hr className="govuk-section-break govuk-section-break--l govuk-section-break--visible" />
        </li>
      ))}
    </ul>
  )
}

export { SkeletonResults }
