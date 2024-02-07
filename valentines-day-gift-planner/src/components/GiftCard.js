import React from 'react';

function GiftCard({ gift }) {
  return (
    <div className="gift-card">
      <img src={gift.imageUrl} alt={gift.name} />
      <h3>{gift.name}</h3>
      <p>{gift.description}</p>
      <button>Buy Now</button>
    </div>
  );
}

export default GiftCard;
