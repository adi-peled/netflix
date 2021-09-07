import React from 'react';
import { MoviePreview } from './MoviePreview';
export const MovieList: React.FC = () => {
  return (
    <div className='movie-list flex'>
      <MoviePreview />
      <MoviePreview />
      <MoviePreview />
    </div>
  );
};
