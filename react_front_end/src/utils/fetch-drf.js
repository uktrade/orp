import { URL, PUBLISHERS } from "./constants"

function buildQuery(filters) {
  const { search, document_type, publisher, sort, page } = filters
  let query = ""

  if (search && search.length > 2) {
    query += `${search}`
  }

  if (page) {
    query += `&page=${page}`
  }

  return query
}

export async function fetchData(filters) {
  const query = buildQuery(filters)
  console.log("Searching for: ", query)

  // const encodedQuery = encodeURI(query)
  const url = `${URL}?query=${query}`

  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error("Network response was not ok")
    }
    const data = await response.json()
    return data
  } catch (error) {
    console.error("There was a problem with your fetch operation:", error)
  }
}
