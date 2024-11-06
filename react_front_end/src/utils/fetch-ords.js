import { DATASET_OBJECT_NAME, URL, DOCUMENT_TYPES, PUBLISHERS } from "./constants"

function buildQuery(filters) {
  console.log("Filters: ", filters)
  const { search, document_type, publisher, sort, page } = filters
  // const limitQuery = ` LIMIT ${numberOfResults}`
  let query = `SELECT c FROM S3Object[*].${DATASET_OBJECT_NAME}[*] c`

  if (search && search.length > 2) {
    query += ` WHERE LOWER(c.title) LIKE LOWER('%${search}%') OR LOWER(c.description) LIKE LOWER('%${search}%')`
  } else {
    query += ` WHERE c.title IS NOT MISSING`
  }

  if (document_type && document_type.length > 0) {
    document_type.map((docType, index) => {
      if (index === 0) {
        query += ` AND c.type = '${docType}'`
      } else {
        query += ` OR c.type = '${docType}'`
      }
    })
  }

  if (publisher && publisher.length > 0) {
    publisher.map((pub, index) => {
      const publisherLabel = PUBLISHERS.find((p) => p.name === pub).label
      if (index === 0) {
        query += ` AND TRIM(c.publisher) = '${publisherLabel}'`
      } else {
        query += ` OR TRIM(c.publisher) = '${publisherLabel}'`
      }
    })
  }

  // if (sort) {
  //   query += ` ORDER BY ${sort}`
  // }

  // if (page) {
  //   query += ` OFFSET ${page}`
  // }

  // query += limitQuery

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
