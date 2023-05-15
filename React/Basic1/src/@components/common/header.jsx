import React from 'react'
import { styled } from 'styled-components';
import { GlobalStyle } from '../../style/globalStyle';
import {theme} from "../../style/theme";

function Header(props) { // 컴포넌트는 항상 대문자!
  const { count, message } = props; // props로 받아온 것은 count이다. Header가 부모에게 받아온 것이다.
  return (
    <MainHeader color={message.color}>
        <h1>{message.title}</h1>
        <p>{count}</p>
    </MainHeader>
  );
}

const MainHeader=styled.header`
    display : flex;
    justify-content : center;
    align-items : center;

    position : sticky;
    top : 0;

    height : 15rem;
    
    color: ${({ color }) => color}; // 대괄호 안의 color가 props로 받은 color이다.

    ${({ theme }) => theme.fonts.title}
    background-color: ${({ theme }) => theme.colors.blue};
`

export default Header;