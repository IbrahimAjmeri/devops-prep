import { add, subtract, multiply } from './calculator';

test('adds two numbers', () => {
    expect(add(2, 3)).toBe(5);
});

test('subtracts two numbers', () => {
    expect(subtract(10, 3)).toBe(7);
});

test('multiplies two numbers', () => {
    expect(multiply(3, 4)).toBe(12);
});