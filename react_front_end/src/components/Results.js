import { SkeletonResults } from "./SkeletonResults"

function Results({ results, isLoading, searchQuery }) {
  if (isLoading) {
    return <SkeletonResults />
  }

  const highlight = (text) => {
    const searchWords = searchQuery.join("|")
    const regex = new RegExp(searchWords, "gi")
    const highlightedText = text.replace(regex, (match) => `<mark>${match}</mark>`)
    return { __html: highlightedText }
  }

  return results ? (
    <div className="govuk-summary-list orp-search-results">
      {results.slice(0, 10).map((result) => {
        const { id, type, title, description, publisher, date_modified, regulatory_topics } = result.c

        // Check if the search term appears within the first 200 characters
        const searchWords = searchQuery.join("|")
        const regex = new RegExp(searchWords, "gi")
        const matchIndex = description.search(regex)

        let concatDescription
        if (matchIndex === -1 || matchIndex <= 200) {
          concatDescription = description.length > 200 ? description.substring(0, 200) + "..." : description
        } else {
          // Adjust the substring to include the highlighted text without cutting off the start
          const start = 0 // Always start from the beginning
          const end = Math.min(description.length, matchIndex + 150) // Include some context after the match
          concatDescription = description.substring(start, end) + "..."
        }

        const highlightedTitle = title ? <span dangerouslySetInnerHTML={highlight(title)} /> : ""
        const highlightedDescription = description ? (
          <span dangerouslySetInnerHTML={highlight(concatDescription)} />
        ) : (
          ""
        )

        const date = new Date(date_modified)
        const govukDate = date.toLocaleDateString("en-GB", {
          day: "numeric",
          month: "long",
          year: "numeric",
        })

        const regulatory_topics_array = regulatory_topics.split("\n")

        return (
          <div className="govuk-summary-list__row--no-border" key={id}>
            <span className="govuk-caption-m">{type}</span>
            <h2 className="govuk-heading-m">
              <a href={`/document/${id}`} className="govuk-link">
                {highlightedTitle}
              </a>
            </h2>
            <p className="govuk-body">{highlightedDescription}</p>
            <p className="govuk-body-s orp-secondary-text-colour govuk-!-margin-bottom-2">Published by: {publisher}</p>
            <p className="govuk-body-s orp-secondary-text-colour">Last updated: {govukDate}</p>
            <ul className="govuk-list orp-topics-list">
              {regulatory_topics_array.map((regulatory_topic, index) => (
                <li key={index} className="govuk-body-s orp-secondary-text-colour">
                  {regulatory_topic}
                </li>
              ))}
            </ul>
            <hr className="govuk-section-break govuk-section-break--l govuk-section-break--visible" />
          </div>
        )
      })}
    </div>
  ) : (
    <p>No results found</p>
  )
}

export { Results }
