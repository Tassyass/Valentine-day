import React, { useEffect, useState } from 'react';
import GiftCard from '../components/GiftCard';
import { fetchGifts } from '../services/apiService';

function GiftListPage() {
  const [gifts, setGifts] = useState([]);

  useEffect(() => {
    async function fetchGiftList() {
      const response = await fetchGifts();
      setGifts(response.data);
    }
    fetchGiftList();
  }, []);

  return (
    <div>
      <h2>Gift List</h2>
      <div className="gift-list">
        {gifts.map((gift) => (
          <GiftCard key={gift.id} gift={gift} />
        ))}
      </div>
    </div>
  );
}

export default GiftListPage;
