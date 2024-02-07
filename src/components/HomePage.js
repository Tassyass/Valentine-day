import jewelryImage from '../assets/jewelry.img';
import chocolatesImage from '../assets/chocolates.img';
import flowersImage from '../assets/flowers.img';
import spaDayImage from '../assets/spa-day.img';
import giftCardsImage from '../assets/gift-cards.img';


const gifts = [
  { name: 'Jewelry', description: 'Beautiful jewelry for your loved one', price: '$50', image: jewelryImage },
  { name: 'Chocolates', description: 'Delicious chocolates to sweeten your day', price: '$20', image: chocolatesImage },
  { name: 'Flowers', description: 'Fresh flowers to brighten any room', price: '$30', image: flowersImage },
  { name: 'Spa Day', description: 'Relaxing spa day for ultimate pampering', price: '$100', image: spaDayImage },
  { name: 'Gift Cards', description: 'Versatile gift cards for any occasion', price: '$50', image: giftCardsImage }
];

const HomePage = () => {
  return (
    <div className="gift-container">
      <h2>Suggested Gifts</h2>
      <div className="gift-list">
        {gifts.map((gift, index) => (
          <div key={index} className="gift-card">
            <img src={gift.image} alt={gift.name} className="gift-image" />
            <div className="gift-details">
              <h3>{gift.name}</h3>
              <p>{gift.description}</p>
              <p>Price: {gift.price}</p>
              <button className="buy-button">Buy</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HomePage;
