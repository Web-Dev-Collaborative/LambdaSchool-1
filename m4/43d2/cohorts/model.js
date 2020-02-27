const db = require('../database/connection.js');

module.exports = {
	getCohorts,
	getCohortStudents,
	getCohort,
	addCohort,
	updateCohort,
	removeCohort
};

// retrieving a list of cohorts
function getCohorts() {
	return db('cohorts');
}

// retrieving a list of students from a cohort
function getCohortStudents(cohortsid) {
	return db('students').where({ 'cohorts.cohortsid': cohortsid });
}

// retrieve cohort
function getCohort(cohortsid) {
	return db('cohorts').where({ 'cohorts.cohortsid': cohortsid });
}

// adding cohort
async function addCohort(cohort) {
	const [id] = await db('cohorts')
		.insert(cohort, 'id')
		.then(ids => {
			return getCohorts();
		});
}

// update cohort
function updateCohort(newCohort, cohortsid) {
	db('cohorts')
		.where({ cohortsid: cohortsid })
		.update(newCohort)
		.then(ids => {
			return ids;
		});
}

// delete cohort
function removeCohort(cohortsid) {
	let cohort = getCohort(cohortsid);
	db('cohorts')
		.delete()
		.where({ cohortsid: cohortsid })
		.then(ids => {
			return cohort;
		});
}
