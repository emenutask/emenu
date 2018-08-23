import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import './List.css'


class List extends Component {
  state = {
    menus: []
  };

  async componentDidMount() {
    fetch('http://127.0.0.1:8000/menu/')
    .then(results  => { return results.json();})
    .then(data => this.setState({
      menus: data.results,
    }))
  }

  render() {
    return (
      <div>
        {this.state.menus.map(item => (
          <div key={item.id} className='menu'>
            <Link to={`/${item.id}`}>
                <h1>{item.name}</h1>
                <span>{item.description}</span>
            </Link>
          </div>
        ))}
      </div>
    );
  }
}

export default List;
