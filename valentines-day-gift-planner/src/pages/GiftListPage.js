import React from 'react';
import { Link } from 'react-router-dom';

function GiftListPage() {
  // Define a list of gifts with their details
  const gifts = [
    {
      name: 'Flowers',
      price: '$20',
      description: 'Beautiful bouquet of fresh flowers.'
    },
    {
      name: 'Chocolates',
      price: '$15',
      description: 'Assorted box of delicious chocolates.'
    },
    {
      name: 'Spa-day',
      price: '$100',
      description: 'Relaxing spa treatment for a day.'
    },
    {
      name: 'Gift Cards',
      price: '$50',
      description: 'Gift card to a favorite store or restaurant.'
    }
  ];

  return (
    <div>
      <h2>Gift List</h2>
      <ul>
        {gifts.map((gift, index) => (
          <li key={index}>
            <h3>{gift.name}</h3>
            <p><strong>Price:</strong> {gift.price}</p>
            <p><strong>Description:</strong> {gift.description}</p>
            {/* Link to the specific gift */}
            <Link to={`/gifts/${gift.name}`}>View Details</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default GiftListPage;
