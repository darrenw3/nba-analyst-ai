export const inchesToFeetAndInches = (inches) => {
    const feet = Math.floor(inches / 12)
    const remainingInches = inches % 12
    return `${feet}' ${remainingInches}"`
}