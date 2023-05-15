import React,  {useState} from 'react'
import { styled } from 'styled-components';
import Header from '../@components/common/header';
import NavWrapper from '../@components/common/nav';
import AsideWrapper from '../@components/common/aside';
import CardSectionWrapper from '../@components/cardsPage/cardSection';

export default function CardsPage() {
  const [count, setCount] = useState(0);
  const [message, setMessage]=useState({
    color: "blue",
    title: "왕감자감자",
  });

  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <>
        <p>{count}</p> 
        <Header count={count} message={message} />
        <ContentWrapper>
            <NavWrapper setCount={setCount} />
            {/* isFlipped 내려주기 */}
            <CardSectionWrapper isFlipped={isFlipped} setIsFlipped={setIsFlipped}/> 
            <AsideWrapper/>   
        </ContentWrapper>
        <footer>낵아 만든 사잍흐</footer>
    </>
  );
}

const ContentWrapper=styled.section`
    display: flex;
`