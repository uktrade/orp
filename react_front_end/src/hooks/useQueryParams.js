import { useState } from "react"

const getQuery = () => {
  if (typeof window !== "undefined") {
    return new URLSearchParams(window.location.search)
  }
  return new URLSearchParams()
}

const getQueryStringVal = (key) => {
  const values = getQuery().getAll(key)
  return values.length > 1 ? values : values[0] || ""
}

const useQueryParams = (key, defaultVal = []) => {
  const initialQuery = getQueryStringVal(key)
  const [query, setQuery] = useState(initialQuery.length ? initialQuery : defaultVal)

  const updateUrl = (newVals) => {
    setQuery(newVals)

    const query = getQuery()

    // Clear existing values for the key
    query.delete(key)

    // Set new values for the key
    if (Array.isArray(newVals)) {
      newVals.forEach((val) => {
        if (typeof val === "string" && val.trim() !== "") {
          query.append(key, val)
        } else if (typeof val === "number") {
          query.append(key, val.toString())
        }
      })
    } else {
      if (typeof newVals === "string" && newVals.trim() !== "") {
        query.append(key, newVals)
      } else if (typeof newVals === "number") {
        query.append(key, newVals.toString())
      }
    }

    if (typeof window !== "undefined") {
      const { protocol, pathname, host } = window.location
      const newUrl = `${protocol}//${host}${pathname}?${query.toString()}`
      window.history.pushState({}, "", newUrl)
    }
  }

  return [query, updateUrl]
}

export { useQueryParams }
