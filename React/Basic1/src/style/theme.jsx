import { css } from "styled-components";

const colors = {
  skyblue: "#E9F3FF",
  blue: "#A6C7EF",
  grey: "#B4B4B4",
  black: "#000000",
};

const fonts = {
  title: css`
    font-family: "KOTRAHOPE";
    font-style: normal;
    font-weight: 800;
    font-size: 4rem;
    letter-spacing: 0.07em;
  `,
  text: css`
    font-family: "KOTRAHOPE";
    font-style: normal;
    font-weight: 500;
    font-size: 1.5rem;
    letter-spacing: 0.07em;
  `,
};

export const theme = {
  colors,
  fonts,
};