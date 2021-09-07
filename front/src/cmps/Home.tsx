import React from 'react';
import { MovieList } from './MovieList';

export const Home: React.FC = () => {
  return (
    <div className='home'>
      <div className='top'>
        <div className='title'></div>
        {/* bgc img */}
        <div className='desc'></div>

        <div className='btns'>
          <button>play</button>
          <button>more info</button>
        </div>
      </div>
      <MovieList />
      <MovieList />
      <MovieList />
      <MovieList />
    </div>
  );
};
