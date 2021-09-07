import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { store } from './store/index';
import './app.scss';
import { Header } from './cmps/Header';
import { Home } from './cmps/Home';
import { MyList } from './cmps/MyList';
function App() {
  return (
    <div className='app'>
      <Router>
        <Header />
        <Switch>
          <Route path='/tv-shows'>
            <Home />
          </Route>
          <Route path='/movies'>
            <Home />
          </Route>
          <Route path='/my-list'>
            <MyList />
          </Route>
          <Route path='/'>
            <Home />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
