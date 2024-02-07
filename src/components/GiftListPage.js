import React, { useState } from 'react';

const GiftListPage = ({ gifts, handleAddGift, handleMarkPurchased }) => {
  const [newGift, setNewGift] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    handleAddGift(newGift);
    setNewGift('');
  };

  return (
    <div>
      <h2>Gift List</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter new gift"
          value={newGift}
          onChange={(e) => setNewGift(e.target.value)}
        />
        <button type="submit">Add Gift</button>
      </form>
      <ul>
        {gifts.map((gift) => (
          <li key={gift.id}>
            <span>{gift.name}</span>
            <button onClick={() => handleMarkPurchased(gift.id)}>Mark Purchased</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GiftListPage;
