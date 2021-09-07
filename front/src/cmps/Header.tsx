import React from 'react';
import './Header.scss';
import { Link } from 'react-router-dom';
export const Header: React.FC = () => {
  return (
    <header className='header flex'>
      <div className='left'>
        <input type='text' placeholder='search' />
      </div>

      <div className='right'>
        <Link to='/my-list'>My list</Link>
        <Link to='/tv-shows'>Tv-Shows</Link>
        <Link to='/movies'>Movies</Link>
        <Link to='/'>Home</Link>
        <img src='' alt='logo' />
      </div>
    </header>
  );
};
