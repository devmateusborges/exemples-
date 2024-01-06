import { User } from '@models/user.entity'

test('it should be ok', () => {
  const user = new User()

  user.firstname = 'Diego'

  expect(user.firstname).toEqual('Diego')
})
