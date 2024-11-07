import { DATASET_OBJECT_NAME, URL, PUBLISHERS } from "./constants"

function buildQuery(filters) {
  const { search, document_type, publisher, sort, page } = filters
  let query = `SELECT c FROM S3Object[*].${DATASET_OBJECT_NAME}[*] c WHERE 1=1`

  if (search && search.length > 2) {
    query += ` AND (LOWER(c.title) LIKE LOWER('%${search}%') OR LOWER(c.description) LIKE LOWER('%${search}%'))`
  }

  if (document_type && document_type.length > 0) {
    const documentTypeQuery = document_type.map((docType) => `c.type = '${docType}'`).join(" OR ")
    query += ` AND (${documentTypeQuery})`
  }

  if (publisher && publisher.length > 0) {
    const publisherQuery = publisher
      .map((pub) => {
        const publisherLabel = PUBLISHERS.find((p) => p.name === pub).label
        return `TRIM(c.publisher) = '${publisherLabel}'`
      })
      .join(" OR ")
    query += ` AND (${publisherQuery})`
  }

  // if (sort) {
  //   query += ` ORDER BY ${sort}`;
  // }

  // if (page) {
  //   query += ` OFFSET ${page}`;
  // }

  return query
}

export async function fetchData(filters) {
  const query = buildQuery(filters)
  const encodedQuery = encodeURI(query)
  const url = `${URL}&query-s3-select=${encodedQuery}`

  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error("Network response was not ok")
    }
    const data = await response.json()
    return data.rows
  } catch (error) {
    console.error("There was a problem with your fetch operation:", error)
  }
}
