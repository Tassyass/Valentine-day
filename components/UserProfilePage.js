
import React from 'react';

const UserProfilePage = ({ userGiftLists }) => {
  return (
    <div>
      <h2>User Profile</h2>
      <h3>Gift Lists:</h3>
      <ul>
        {userGiftLists.map((list) => (
          <li key={list.id}>
            <h4>{list.title}</h4>
            <p>{list.description}</p>
            <p>Budget: ${list.budget}</p>
            <ul>
              {list.gifts.map((gift) => (
                <li key={gift.id}>
                  <span>{gift.name}</span>
                  <p>{gift.description}</p>
                  <img src={gift.image} alt={gift.name} />
                  <p>Price: ${gift.price}</p>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserProfilePage;
