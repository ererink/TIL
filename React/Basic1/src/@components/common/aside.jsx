import React from 'react'
import { styled } from 'styled-components';
import { GlobalStyle } from '../../style/globalStyle';
import {theme} from "../../style/theme";


function Aside() {
  return (
    <AsideWrapper>
        <ul>
            <li>업로드 페이지</li>
            <li>마이 페이지</li>
            <li>로그아웃</li>
        </ul>
    </AsideWrapper>
  )
}

const AsideWrapper=styled.aside`
    width: 20%;
    height: 20rem;
    background-color: skyblue;

    ${({ theme }) => theme.fonts.title}

`;
export default Aside

