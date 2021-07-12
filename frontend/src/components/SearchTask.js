import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';

const SearchTask = () => {

  const [searchTerm, setSearchTerm] = useState('')
  const history = useHistory();

  function backClick () {
    history.push('./taskboard')
  }

  function handleSearch() {
    history.push({
      pathname: './taskSearchResult',
      search: searchTerm
    })
  }

  return(
    <>
     <div className="input-group mb-3">
      <input type="text" placeholder="Search Task by id, name, description or deadline" onChange={(e) => setSearchTerm(e.target.value)} className="form-control" aria-label="" aria-describedby="basic-addon1"></input>
      <div className="input-group-prepend">
        <button className="btn btn-outline-secondary" type="button" onClick={() => handleSearch()}>Search</button>
      </div>
    </div>
    </>
  )
}

export default SearchTask