import React from 'react'
import { styled } from 'styled-components';
import { GlobalStyle } from '../../style/globalStyle';
import {theme} from "../../style/theme";

function Nav(props) {
  const {setCount} = props;

  function updateCnt(){
    setCount((prev) => prev + 1); // 이전의 값에서 + 1 하겠다!
  }

  return (
    <NavWrapper onClick={updateCnt}>
        <ul>
            <li>전체보기</li>
            <li>행복 루피 보기</li>
            <li>짜증 루피 보기</li>
        </ul>
    </NavWrapper>
  );
}

const NavWrapper=styled.nav`
    width: 20%;
    height: 20rem;
    background-color: skyblue;

    ${({ theme }) => theme.fonts.title}

`;
export default Nav;