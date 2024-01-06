import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const ThemeStore = createSlice({
  name: "theme",

  initialState: {
    classNameBorder: "border-blue-400",
    classNameText: "text-blue-400",
    classNameBg: "bg-blue-400",
    classNameTitleText: "text-0",
    classNameTitleBg: "bg-blue-400",
  },
  reducers: {
    classNameAction(
      state: Record<string, string>,
      action: PayloadAction<Array<string>>
    ) {
      const [className, classValue] = action.payload;
      state[className] = classValue;
    },
  },
});

export const { classNameAction } = ThemeStore.actions;

export default ThemeStore.reducer;
