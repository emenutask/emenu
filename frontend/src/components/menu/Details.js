import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import './Details.css';


class Details extends Component {
  state = {
    name: null,
    dishes: [],
  };

  async componentDidMount() {
    const id = this.props.match.params.id;
    fetch(`http://127.0.0.1:8000/menu/${id}/`)
    .then(results  => { return results.json();})
    .then(data => this.setState({
      name: data.name,
      dishes: data.dish_set
    }))
  }

  render() {
    return (
      <div>
        <h1>{this.state.name}</h1>
        {this.state.dishes.map(item => (
          <div key={item.id} className='dish'>
            <h3>{item.name}</h3>
            <span className='price'>{item.price}</span>
            <div>{item.description}</div>
          </div>
        ))}
        <Link to=''>Back</Link>
      </div>
    );
  }
}

export default Details;
