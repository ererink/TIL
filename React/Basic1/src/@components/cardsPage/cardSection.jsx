import React from 'react'
import { styled } from 'styled-components'
import Card from './card'
import { CARDS_LIST } from '../../core/cardsData'

function CardSection(props) {
  const {isFlipped, setIsFlipped } = props;
  return (
    <CardSectionWrapper>
        {/* map == for문 */}
        {CARDS_LIST.map((cards)=>(
        <Card 
            id={cards.id} 
            name={cards.name} 
            img={cards.img} 
            isFlipped={isFlipped} 
            setIsFlipped={setIsFlipped}/>
        ))} 
        
    </CardSectionWrapper>
  )
}

const CardSectionWrapper=styled.section`
    display: flex;
    flex-wrap: wrap;
    width: 60%;

    background-color: pink;
`

export default CardSection