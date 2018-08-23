import React from 'react';
import { Route } from 'react-router-dom';

import Details from './menu/Details';
import List from './menu/List';

class App extends React.Component {
  render() {
    return (
      <div>
           <Route exact path="/" component={List}/>
           <Route exact path="/:id" component={Details}/>
      </div>
    )
  }
}

export default App;
