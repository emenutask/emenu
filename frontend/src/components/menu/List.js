import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import './List.css'


class List extends Component {
  state = {
    menus: [],
    sortingHumanName: 'id',
    sortingName: null
  };

  constructor(props) {
    super(props);
    this.handleClickOutside = this.handleClickOutside.bind(this);
  };

  async componentDidMount() {
    this.getMenus();
    document.addEventListener('click', this.handleClickOutside);
  };

  componentWillUnmount() {
    document.removeEventListener('click', this.handleClickOutside);
  };

  getMenus(sorting) {
    let url = 'http://127.0.0.1:8000/menu/';
    if (sorting){
      url = url.concat(`?ordering=${sorting}`);
    }
    fetch(url)
    .then(results  => { return results.json();})
    .then(data => this.setState({
      menus: data.results,
    }))
  };

  openDropdown() {
    document.getElementById('myDropdown').classList.toggle('show');
  };

  handleClickOutside(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName('dropdown-content');
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  };

  updateSorting(name, humanName) {
    this.setState({sortingHumanName: humanName, sortingName: name});
    this.getMenus(name);
  };

  render() {
    return (
      <div>
        <div className='sorting'>
          sort by
          <div className='dropdown'>
            <button onClick={this.openDropdown} className='dropbtn'>{this.state.sortingHumanName}</button>
            <div id='myDropdown' className='dropdown-content'>
              <a onClick={() => this.updateSorting('name', 'names asc')}>name asc</a>
              <a onClick={() => this.updateSorting('-name', 'name desc')}>name desc</a>
              <a onClick={() => this.updateSorting('dishes_count', 'number of dishes asc')}>number of dishes asc</a>
              <a onClick={() => this.updateSorting('-dishes_count', 'number of dishes desc')}>number of dishes desc</a>
            </div>
          </div>
        </div>
        <div className='clearfix'/>

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
