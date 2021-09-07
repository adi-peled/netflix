import React, { useState } from 'react';

export const MoviePreview: React.FC = () => {
  const [isHover, setIsHover] = useState<Boolean>(false);
  return (
    <div
      className='movie-preview'
      onMouseEnter={() => setIsHover(true)}
      onMouseLeave={() => setIsHover(false)}
    >
      <img src='' alt='' />
      preview for now
      {isHover && (
        <div className='hover'>
          <div className='btns'>
            <button className='btn-info'>more info</button>
            <button className='btn-play'>play</button>
          </div>
          <div className='details'>
            <span className='age'>+16</span>
            <span className='during'> 110 min</span>
          </div>
          <div className='genres'>
            <span> action</span>
            <span>adventure</span>
          </div>
        </div>
      )}
    </div>
  );
};
