import { useState } from 'react';

const getQuery = () => {
  if (typeof window !== 'undefined') {
    return new URLSearchParams(window.location.search);
  }
  return new URLSearchParams();
};

const getQueryStringVal = key => {
  return getQuery().getAll(key);
};

const useQueryParams = (key, defaultVal = []) => {
  const [query, setQuery] = useState(getQueryStringVal(key).length ? getQueryStringVal(key) : defaultVal);

  const updateUrl = (newVals) => {
    setQuery(newVals);

    const query = getQuery();

    // Clear existing values for the key
    query.delete(key);

    // Set new values for the key
    newVals.forEach(val => {
      if (val.trim() !== '') {
        query.append(key, val);
      }
    });

    if (typeof window !== 'undefined') {
      const { protocol, pathname, host } = window.location;
      const newUrl = `${protocol}//${host}${pathname}?${query.toString()}`;
      window.history.pushState({}, '', newUrl);
    }
  };

  return [query, updateUrl];
};

export { useQueryParams };