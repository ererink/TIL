import React from 'react'
import { styled } from 'styled-components'
import { useEffect } from 'react';

function Card(props) {
  const { id, name, img, isFlipped, setIsFlipped } = props;
  const [isChanged, setIsChanged] = useState(false);
  const [count, setcount] = useState(0);

  function flipCard() {
    setIsFlipped(!isFlipped);
    setIsChanged(!isChanged);
    setcount(count + 1);
  }

  useEffect(() => {
    count===10 && alert("축하합니다!")
  }, [isChanged]);

  return (
    <article onClick={flipCard}>
        {isFlipped ? (
            <div>뒤집어놓으셔따</div>
        ) : (
        <CardWrapper>
            <h1>{name}</h1>
            <img src={img} alt={name} />
        </CardWrapper>
        )}
    </article> 
  );
}

const CardWrapper=styled.article`
    width: 20rem;
    height: 20rem;
    background-color: aquamarine;
`

export default Card