import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const CrudStore = createSlice({
  name: "crud",

  initialState: {
    dataSelected: {} as any,
  },
  reducers: {
    dataSelectedAction(state, action: PayloadAction<any>) {
      // console.log("CrudStore>dataSelected-1", action.payload);
      const newSelected = action.payload;
      state.dataSelected = { ...state.dataSelected, ...newSelected };
      // console.log("CrudStore>dataSelected-2", state.dataSelected);
    },
    dataSelectedCleanAllAction(state) {
      state.dataSelected = [];
    },
    dataSelectedCleanAction(state, action: PayloadAction<string>) {
      state.dataSelected[action.payload] = [];
    },
  },
});

export const {
  dataSelectedAction,
  dataSelectedCleanAllAction,
  dataSelectedCleanAction,
} = CrudStore.actions;

export default CrudStore.reducer;
