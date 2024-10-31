const Results = ({ searchQuery, docTypeQuery, publisherQuery, pageQuery, sortQuery }) => (
  <div>
    <h2 className="govuk-heading-m">Results</h2>
    <pre>
      <p>Search query: {searchQuery.join(", ")}</p>
      <p>Document type: {docTypeQuery.join(", ")}</p>
      <p>Published by: {publisherQuery.join(", ")}</p>
      <p>Page: {pageQuery.join(", ")}</p>
      <p>Sort: {sortQuery.join(", ")}</p>
    </pre>
  </div>
)

export { Results }
